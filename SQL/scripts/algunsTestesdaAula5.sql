create table cpfs
(
	id int unsigned not null,
    cpf varchar (14) not null,
    primary key (id),
    constraint fk_cpf foreign key (id) references funcionarios (id)
);

insert into cpfs (id, cpf) values (1, '111-111-111-11');
insert into cpfs (id, cpf) values (2, '222-222-222-22');
insert into cpfs (id, cpf) values (3, '333-333-333-33');
insert into cpfs (id, cpf) values (4, '444-444-444-44');

select * from cpfs c inner join funcionarios f on f.id = c.id;
select * from cpfs c inner join funcionarios f using(id);

create table clientes
(
	id int unsigned not null auto_increment,
    nome varchar (45) not null,
    quem_indicou int unsigned,
    primary key (id),
    constraint fk_quem_indicou foreign key (quem_indicou) references clientes (id)
);

insert into clientes (id, nome, quem_indicou) VALUES (1, 'André', NULL);
insert into clientes (id, nome, quem_indicou) VALUES (2, 'Carlos', 1);
insert into clientes (id, nome, quem_indicou) VALUES (3, 'Samuel', 2);
insert into clientes (id, nome, quem_indicou) VALUES (4, 'Rafael', 2);

select * from clientes;

select a.nome indicado, b.nome indicou from clientes a join clientes b on a.quem_indicou = b.id; #self join


create view vw_teste as
select 
	f.nome,
    c.cpf,
    v.veiculo
from cpfs c 
inner join funcionarios f on f.id = c.id
left join veiculos v on v.funcionario_id = c.id;