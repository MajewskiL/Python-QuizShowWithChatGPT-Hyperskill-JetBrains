from hstest import StageTest, TestedProgram, CheckResult, dynamic_test


class TestQuizShow(StageTest):
    @dynamic_test
    def testExitWithName(self):
        program = TestedProgram()
        program.start()

#        program.execute("egg")

#        exit_output = program.execute("exit")
#        if "egg" not in exit_output:
#            return CheckResult.wrong("No Egg!")

        return CheckResult.correct()
