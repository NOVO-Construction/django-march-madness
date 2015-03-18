-- Application: madness
-- Model: Game
ALTER TABLE `madness_game`
	ADD COLUMN `winner_id` integer REFERENCES `madness_bracket` (`id`);
CREATE INDEX `madness_game_winner_id`
	ON `madness_game` (`winner_id`);
-- Model: Entry
ALTER TABLE `madness_entry`
	ADD COLUMN `prev_position` integer NOT NULL;
ALTER TABLE `madness_entry`
	ADD COLUMN `possible` integer NOT NULL;
ALTER TABLE `madness_entry`
	ADD COLUMN `points` integer NOT NULL;
ALTER TABLE `madness_entry`
	ADD COLUMN `position` integer NOT NULL;