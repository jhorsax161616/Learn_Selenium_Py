from unittest import TestLoader, TestSuite, runner
from pyunitreport import HTMLTestRunner
from assertions import AssertionsTest
from searchtests import SearchTests

assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_test = TestLoader().loadTestsFromTestCase(SearchTests)

#construyendo la suite de prubas
smoke_test = TestSuite([assertions_test, search_test])

#Generando reportes
kwargs = {
    "output": 'smoke-report'
}

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)
