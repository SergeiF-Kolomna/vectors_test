import unittest

class TestVector3D(unittest.TestCase):
    def setUp(self):
        self.v1 = Vector3D(1, 2, 3)
        self.v2 = Vector3D(2, 4, 6)
        self.v3 = Vector3D(-1, -2, -3)
    
    def test_scalar_product(self):
        self.assertEqual(self.v1.dot_product(self.v2), 28)
    
    def test_cross_product(self):
        self.assertEqual(self.v1.cross_product(self.v2), Vector3D(0, 0, 0))
    
    def test_length(self):
        self.assertAlmostEqual(self.v1.length(), math.sqrt(14))
    
    def test_angle_between(self):
        self.assertAlmostEqual(self.v1.angle_between(self.v2), 0.0)
        self.assertAlmostEqual(self.v1.angle_between(self.v3), 180.0)
    
    def test_collinearity(self):
        self.assertTrue(self.v1.is_collinear(self.v2))
        self.assertTrue(self.v2.is_collinear(self.v1))
        self.assertTrue(self.v1.is_collinear(Vector3D(2, 4, 6)))
        self.assertFalse(self.v1.is_collinear(self.v3))

if __name__ == '__main__':
    unittest.main()

