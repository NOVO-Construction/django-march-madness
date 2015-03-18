-- Application: madness
-- Model: Bracket
ALTER TABLE `madness_bracket`
	ADD COLUMN `is_eliminated` bool NOT NULL;
