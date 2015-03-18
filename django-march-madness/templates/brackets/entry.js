window.MM = window.MM || {};

MM.EntryPick = Backbone.Model.extend({
  urlRoot: 'ajax/'
});
MM.EntryPickCollection = Backbone.Collection.extend({
  model: MM.EntryPick,
  url: 'ajax/'
});

MM.EntryPickView = Backbone.View.extend({
  events: {
    'click': 'click',
  },
  initialize: function () {
    var el = '#w' + this.model.get('game_pk');
    this.$el = $(el);
  },
  render: function () {
    this.$el.text(this.model.get('pick_team_display'));
    this.$el.prop('title', this.model.get('pick_team_display'));
    return this;
  },
  click: function (event) {
    var that = this;
    var data = JSON.stringify({
      pick: this.model.get('pick_pk'),
      game: this.$el.closest('ul').data('game')
    });
    $.post('ajax/', data, function(data) {
      that.collection.fetch({reset: true});
    });
  },
});

MM.EntryPickCollectionView = Backbone.View.extend({
  el: $('.bracket'),
  initialize: function () {
    this.listenTo(this.collection, 'reset', this.render);
    this._views = [];
  },
  render: function () {
    _.each(this._views, function (view) {
      view.undelegateEvents();
      view.$el.empty();
    });
    this.addAll();
    return this;

  },
  addOne: function (model) {
    var el = '#w' + model.get('game_pk');
    var view = new MM.EntryPickView({model: model, collection: this.collection, el: el});
    this._views.push(view);
    view.render();
  },
  addAll: function () {
    this.collection.forEach(this.addOne, this);
  }
});

MM.App = Backbone.Router.extend({
  initialize: function () {
    var that = this;
    this.entryPickCollection = new MM.EntryPickCollection();
    this.entryPickCollection.fetch({reset: true});

    this.entryPickCollectionView = new MM.EntryPickCollectionView({collection: this.entryPickCollection});

    $('[name=tie_break]').bind('keyup paste', function() {
      setTimeout($.proxy(function() {
        var value = this.val().replace(/[^0-9]/g, '');
        var data = JSON.stringify({
          tie_break: value
        });
        $.post('ajax/', data, function(data) {
          that.entryPickCollection.fetch({reset: true});
        });
        this.val(value);
      }, $(this)), 0);
    });

    $('[data-round="1"] .team.pickable').click(function() {
      var game = $(this).parent().parent().data('game');
      var pick = $(this).data('id');
      var data = JSON.stringify({
        pick: pick,
        game: game
      });
      $.post('ajax/', data, function(data) {
        that.entryPickCollection.fetch({reset: true});
      });
    });

    $.each($('[data-round="1"] .team'), function() {
      $(this).prop('title', $(this).text());
    });
  }
});
MM.app = new MM.App();
