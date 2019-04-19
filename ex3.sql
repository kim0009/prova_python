-- opção 1 -> considere essa a minha resposta
UPDATE pessoa SET cpf = '' + SUBSTRING(cpf, 1, 3) + '.' + SUBSTRING(cpf, 4, 3) + '.' + SUBSTRING(cpf, 8, 3) + '-' + SUBSTRING(cpf, 10, 2)
	WHERE  cpf NOT LIKE '___%.___%.___%-__'

-- opção 2
UPDATE pessoa SET cpf = '' + SUBSTRING(cpf, 1, 3) + '.' + SUBSTRING(cpf, 4, 3) + '.' + SUBSTRING(cpf, 8, 3) + '-' + SUBSTRING(cpf, 10, 2)
	WHERE  cpf in (
	SELECT pes.cpf FROM cliente AS cli
		JOIN pessoa AS pes 
		ON cli.id_customers = pes.id_customers
		WHERE  pes.cpf NOT LIKE '___%.___%.___%-__'
	)  