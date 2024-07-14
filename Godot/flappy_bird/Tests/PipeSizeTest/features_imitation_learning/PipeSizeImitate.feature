Feature: Flappy Bird Game Imitated

	@manual
	Scenario: Testing the pipe size
		Given first pipe at 0 and second pipe at 1
		When bird flies using ./Tests/PipeSizeTest/models/fly/bc_policy.zip model
		Then bird should have passed 2 pipes

	@manual
	Scenario: Testing the pipe size 2
		Given first pipe at 1 and second pipe at 0
		When bird flies using ./Tests/PipeSizeTest/models/fly/bc_policy.zip model
		Then bird should have passed 2 pipes
