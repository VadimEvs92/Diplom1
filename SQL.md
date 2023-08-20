
SELECT "track", CASE WHEN finished = 'true' THEN 'status = 2' WHEN cancelled = 'true' THEN 'status = 1' WHEN "inDelivery" = 'true' THEN 'status = 1' ELSE 'status = 0' END FROM "Orders";

SELECT c."login", COUNT(o."track") FROM "Couriers" as c INNER JOIN "Orders" as o on c."courierId" WHERE "inDelivery" = true GROUP BY login;

