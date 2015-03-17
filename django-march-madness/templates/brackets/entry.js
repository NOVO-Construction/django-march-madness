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
    console.log('render collection', this.collection);
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
    this.entryPickCollection = new MM.EntryPickCollection();
    this.entryPickCollection.fetch({reset: true});

    this.entryPickCollectionView = new MM.EntryPickCollectionView({collection: this.entryPickCollection});
  }
});
MM.app = new MM.App();
