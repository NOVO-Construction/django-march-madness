window.MM = window.MM || {};

MM.EntryPick = Backbone.Model.extend({
  urlRoot: 'ajax/'
});
MM.EntryPickCollection = Backbone.Collection.extend({
  model: MM.EntryPick,
  url: 'ajax/'
});

MM.Game = Backbone.Model.extend({
  urlRoot: '/madness/games/ajax/'
});
MM.GameCollection = Backbone.Collection.extend({
  model: MM.Game,
  url: '/madness/games/ajax/'
});

MM.PickCountView = Backbone.View.extend({
  el: '#pick-count',
  initialize: function () {
    this.listenTo(this.collection, 'reset', this.render);
  },
  render: function () {
    var length = MM.app.entryPickCollection.length;
    this.$('.count').text(length);
    if (length < 63) {
      this.$('.btn').addClass('btn-danger');
      this.$('.btn').removeClass('btn-success');
    } else {
      this.$('.btn').removeClass('btn-danger');
      this.$('.btn').addClass('btn-success');
    }
    return this;
  }
});

MM.EntryPickView = Backbone.View.extend({
  initialize: function () {
    var el = '#w' + this.model.get('game_pk');
    this.$el = $(el);
  },
  render: function () {
    this.$el.text(this.model.get('pick_team_display'));
    this.$el.prop('title', this.model.get('pick_team_display'));
    return this;
  }
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
    $('.bracket .team').removeClass('pickable');
  }
});

MM.App = Backbone.Router.extend({
  initialize: function () {
    var that = this;
    this.entryPickCollection = new MM.EntryPickCollection();
    this.entryPickCollection.fetch({reset: true});

    this.gameCollection = new MM.GameCollection();
    this.gameCollection.fetch({reset: true});

    this.entryPickCollectionView = new MM.EntryPickCollectionView({collection: this.entryPickCollection});
    this.pickCountView  = new MM.PickCountView({collection: this.entryPickCollection});

    $('[name=tie_break]').prop('disabled', true);

    $.each($('[data-round="1"] .team'), function() {
      $(this).prop('title', $(this).text());
    });
  }
});
MM.app = new MM.App();
