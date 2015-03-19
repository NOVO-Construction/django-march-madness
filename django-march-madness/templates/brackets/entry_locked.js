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
  url: '/madness/games/ajax/',
  finished: function() {
    var filtered = this.filter(function(item) {
      return item.get('winner');
    });
    return new MM.GameCollection(filtered);
  },
  unfinished: function() {
    var filtered = this.filter(function(item) {
      return item.get('winner') === null;
    });
    return new MM.GameCollection(filtered);
  }
});

MM.PickCountView = Backbone.View.extend({
  el: '#pick-count',
  initialize: function () {
    this.listenTo(this.collection, 'reset', this.render);
  },
  render: function () {
    var length = this.collection.length;
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

MM.MarkGamesView = Backbone.View.extend({
  el: $('.bracket'),
  initialize: function () {
    this.listenTo(this.collection, 'reset', this.render);
  },
  render: function () {
    console.log('render MarkGamesView');
    this.finished = this.collection.finished();
    this.unfinished = this.collection.unfinished();
    this.markFinished();
    this.markUnfinished();
    return this;
  },
  markFinished: function () {
    this.finished.each(function(game) {
      var gameSelector = '[data-game="' + game.get('pk') + '"]';
      var winnerSelector = '[data-id="' + game.get('winner').pk + '"]';
      $game = this.$(gameSelector);
      $winner = this.$(winnerSelector);
      $game.addClass('finished');
      $winner.addClass('winner');
      $game.find('.team:not(.winner)').addClass('loser');

      // console.log(game.get('winner').pk);

      // $winner = $('#w' + game.get('pk'));
      // $winner.addClass('correct');
      // $winner.addClass('incorrect');
      // console.log($game, $winner);
    }, this);
  },
  markUnfinished: function () {
    this.unfinished.each(function(game) {
      var gameSelector = '[data-game="' + game.get('pk') + '"]';
      $game = this.$(gameSelector);
      $game.addClass('unfinished');
      // $winner = $('#w' + game.get('pk'));
      // $winner.addClass('correct');
      // $winner.addClass('incorrect');
      // console.log($game, $winner);
    }, this);
  }
});

MM.App = Backbone.Router.extend({
  initialize: function () {
    var that = this;
    this.entryPickCollection = new MM.EntryPickCollection();
    this.entryPickCollection.fetch({reset: true});

    this.entryPickCollectionView = new MM.EntryPickCollectionView({collection: this.entryPickCollection});
    this.pickCountView  = new MM.PickCountView({collection: this.entryPickCollection});

    this.gameCollection = new MM.GameCollection();
    this.gameCollection.fetch({reset: true});
    this.markGamesView  = new MM.MarkGamesView({collection: this.gameCollection});

    $('[name=tie_break]').prop('disabled', true);

    $.each($('[data-round="1"] .team'), function() {
      $(this).prop('title', $(this).text());
    });
  }
});
MM.app = new MM.App();
