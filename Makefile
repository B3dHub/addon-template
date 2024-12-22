wheel:
	python setup.py build bdist_wheel
	if not exist wheels mkdir wheels
	if exist dist\*.whl cmd /c "move dist\*.whl wheels"
	cmd /c "rmdir /s /q build dist qbpy.egg-info"