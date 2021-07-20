insert into funcionarios (id, nome, salario, departamento, data_nasc) values( 1, 'Fernando Pessoa', 1400, 'TI', '1984-05-14');
insert into funcionarios (nome, salario, departamento, data_nasc) values( 'Guilherme Azevedo', 2500, 'TI', '1980-08-20');
insert into funcionarios (nome, salario, departamento, data_nasc) values( 'Tomas cat', 8000, 'Vendas', '2000-01-20');
insert into funcionarios (nome, salario, departamento, data_nasc) values( 'Che cat Luiza', 5000, 'Segurança', '1995-05-14');

select * from veiculos;

set sql_safe_updates = 0;  #comando para tirar restrição de (sem where) para atualizar tabela toda.

update funcionarios set salario = round( salario * 1.1, 2); #round para arrendodar valores (passar casas decimais depois da virgula)

insert into veiculos (funcionario_id, veiculo, placa) values (1, 'Fusca', 'abc1234');
insert into veiculos (funcionario_id, veiculo, placa) values (1, 'Chevette', 'abc1235');

update veiculos set funcionario_id = 4 where id = 2;

insert into salarios (faixa, inicio, fim) values ('Analista jr', 1000, 2000);
insert into salarios (faixa, inicio, fim) values ('Analista Pleno', 2000, 4000);

select * from funcionarios f where salario > 2000;

select nome as 'Funcionario', salario from funcionarios f where f.salario >2000;

select * from funcionarios where nome = 'Tomas cat'
union
select * from funcionarios where id = 4;

update funcionarios set salario = salario * 1.1;