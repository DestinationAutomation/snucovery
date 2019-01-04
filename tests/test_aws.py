import unittest
import pytest
import os
from botocore.exceptions import ProfileNotFound, UnknownServiceError
from snucovery.aws import AwsServices
from snucovery.errors import (
    UnknownServiceCall, InvalidServiceMappings
)


SKIP_INTEGRATION = os.getenv('SKIP_INTEGRATION', True)
class TestAwsServices(unittest.TestCase):
    @unittest.skipIf(SKIP_INTEGRATION, "Skipping integratration tests")
    def test_init_aws_service(self):
        aws = AwsServices('test')
        self.assertIsInstance(aws, object)
        self.assertTrue(aws.session)

    @unittest.skipIf(SKIP_INTEGRATION, "Skipping integratration tests")
    def test_init_aws_service_fail(self):
        with self.assertRaises(ProfileNotFound):
            AwsServices('test-fail')

    @unittest.skipIf(SKIP_INTEGRATION, "Skipping integratration tests")
    def test_get_service_mappings(self):
        aws = AwsServices('test')
        self.assertGreater(len(aws.get_service_mappings()), 0)

    @unittest.skipIf(SKIP_INTEGRATION, "Skipping integratration tests")
    def test_get_service_mappings_empty(self):
        aws = AwsServices('test')
        aws.service_mappings = {}
        with self.assertRaises(InvalidServiceMappings):
            aws.get_service_mappings()

    @unittest.skipIf(SKIP_INTEGRATION, "Skipping integratration tests")
    def test_scan_services(self):
        aws = AwsServices('test')
        items = aws.scan_services()
        self.assertGreater(len(items), 0)

    @unittest.skipIf(SKIP_INTEGRATION, "Skipping integratration tests")
    def test_scan_service(self):
        aws = AwsServices('test')
        items = aws.scan_service('describe_instances', 'ec2')
        self.assertGreater(len(items), 0)

    @unittest.skipIf(SKIP_INTEGRATION, "Skipping integratration tests")
    def test_scan_service_raise_service_error(self):
        aws = AwsServices('test')
        with self.assertRaises(UnknownServiceError):
            aws.scan_service('describe_instances', 'ec22')

    @unittest.skipIf(SKIP_INTEGRATION, "Skipping integratration tests")
    def test_scan_service_raise_unknown_service_call(self):
        aws = AwsServices('test')
        with self.assertRaises(UnknownServiceCall):
            aws.scan_service('describe_instanes', 'ec2')
