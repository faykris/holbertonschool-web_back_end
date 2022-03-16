-- 2. Best band ever!
-- ranks country origins of bands, ordered by the number of (non-unique) fans
SELECT origin, SUM(fans) AS n_fans
FROM metal_bands
GROUP BY origin
ORDER BY n_fans DESC;
