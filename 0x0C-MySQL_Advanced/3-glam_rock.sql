-- 3. Old school band
-- lists all bands with Glam rock as their main style, ranked by their longevity

CREATE PROCEDURE years (IN band VARCHAR(255), OUT lifespan INT)
BEGIN
	SELECT COUNT(*) FROM metal_bands WHERE style LIKE '%"@band"%'
END
