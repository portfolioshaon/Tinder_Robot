for /f "tokens=*" %a in (prm/project.log) do (
	if "%a" == "[initialized]" (
		echo yes
	) else (
		git init
		SET /P repon=Repository name:
		SET /P repol=Repository link:
		git add remote %repon% %repol%
		
	)
)