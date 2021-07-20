/* create usaer 'lola'@'192.168.1.1' identified by '123456';
create usaer 'lola'@'%' identified by '123456'; */

create user 'lola'@'localhost' identified by '123456';
grant all on curso_sql.* to 'lola'@'localhost';

create user 'lola'@'%' identified by '123456';
grant select on curso_sql.* to 'lola'@'%';
grant insert on curso_sql.funcionarios to 'lola'@'%';

revoke insert on curso_sql.funcionarios from 'lola'@'%';

drop user 'lola'@'%';

select user from mysql.user;

show grants for 'lola';