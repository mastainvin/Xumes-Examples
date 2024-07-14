Feature: Flappy Bird Game


	@easy @smoke
	Scenario Outline: Testing the pipe size easy
		Given first pipe at <i> and second pipe at <j>
		When bird flies
		Then bird should have passed <k> pipes


		Examples:
			| i   | j   | k |
			| 0   | 0   | 2 |
			| 0.5 | 0.5 | 2 |
			| 1   | 1   | 2 |


	Scenario Outline: Testing the pipe size
		Given first pipe at <i> and second pipe at <j>
		When bird flies
		Then bird should have passed <k> pipes


		Examples:
			| i   | j   | k |
			| 0   | 0.5 | 2 |
			| 0.5 | 0   | 2 |
			| 0.5 | 1   | 2 |
			| 1   | 0.5 | 2 |


	@hard
	Scenario Outline: Testing the pipe size hard
		Given first pipe at <i> and second pipe at <j>
		When bird flies
		Then bird should have passed <k> pipes


		Examples:
			| i   | j   | k |
			| 0   | 1   | 2 |
			| 1   | 0   | 2 |
