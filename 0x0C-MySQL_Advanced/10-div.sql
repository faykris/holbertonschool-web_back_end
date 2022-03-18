-- 10. Safe divide
-- Function that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.

DELIMITER $$

DROP FUNCTION IF EXISTS SafeDiv;

CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS FLOAT DETERMINISTIC
BEGIN
	IF b = 0 THEN
		RETURN 0;
	END IF;
	RETURN a / b;
END

$$

DELIMITER ;
