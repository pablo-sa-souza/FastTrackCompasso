select * from funcionarios;
select count(*) from funcionarios where departamento = 'ti';
select sum(salario) from funcionarios where departamento = 'ti';

select departamento, avg(salario) from funcionarios group by departamento;

select departamento, avg(salario) from funcionarios group by departamento having avg(salario) > 3000;

select departamento, count(*) from funcionarios group by departamento;

select departamento, nome from funcionarios
	where departamento in 
		(
		select departamento from funcionarios group by departamento having (salario) > 2000
        );