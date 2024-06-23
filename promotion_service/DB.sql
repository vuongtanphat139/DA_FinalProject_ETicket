-- ALTER event
-- INSERT INTO 'event' ('event_id', 'name', 'description', 'numberOfTicket', 'address') VALUES
-- (1, "Su kien 1", "Mo ta cua su kien 1", 100, "TPHCM"),
-- (2, "Su kien 2", "Mo ta cua su kien 2", 100, "HaNoi"),
-- (3, "Su kien 3", "Mo ta cua su kien 3", 100, "DaNang"),
-- (4, "Su kien 4", "Mo ta cua su kien 4", 100, "TPHCM"),
-- (5, "Su kien 5", "Mo ta cua su kien 5", 100, "TPHCM")

-- INSERT INTO `event` (`event_id`, `name`, `description`, `numberOfTicket`, `address`) VALUES
-- (1, 'Su kien 1', 'Mo ta cua su kien 1', 100, 'TPHCM'),
-- (2, 'Su kien 2', 'Mo ta cua su kien 2', 100, 'HaNoi'),
-- (3, 'Su kien 3', 'Mo ta cua su kien 3', 100, 'DaNang'),
-- (4, 'Su kien 4', 'Mo ta cua su kien 4', 100, 'TPHCM'),
-- (5, 'Su kien 5', 'Mo ta cua su kien 5', 100, 'TPHCM');
-- select * from event

-- INSERT INTO incentive('incentive_id', 'event_id', 'discount', 'description', 'deleted', 'version') VALUES
-- (1, 1, 0.1, '10% discount', 0, 1),
-- (2, 1, 0.15, '15% discount', 0, 1),
-- (3, 4, 0.2, '20% discount', 0, 1),
-- (4, 4, 0.25, '25% discount', 0, 1),
-- (5, 4, 0.3, '30% discount', 0, 1);
-- (6, 5, 0.1, '10% discount', 0, 1),

-- INSERT INTO incentive (incentive_id, event_id, discount, description, deleted, version) VALUES
-- (1, 1, 0.1, '10% discount', 0, 1),
-- (2, 1, 0.15, '15% discount', 0, 1),
-- (3, 4, 0.2, '20% discount', 0, 1),
-- (4, 4, 0.25, '25% discount', 0, 1),
-- (5, 4, 0.3, '30% discount', 0, 1),
-- (6, 5, 0.1, '10% discount', 0, 1);

select * from incentive