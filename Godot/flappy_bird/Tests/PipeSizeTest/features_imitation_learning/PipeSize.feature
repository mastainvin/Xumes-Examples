Feature: Flappy Bird Game


	@manual
	Scenario: Testing the pipe size
		Given first pipe at 0 and second pipe at 1
		When bird flies using new model
		Then bird should have passed 2 pipes

	@manual
	Scenario: Testing the pipe size 2
		Given first pipe at 1 and second pipe at 0
		When bird flies using new model
		Then bird should have passed 2 pipes