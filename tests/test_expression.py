#! /usr/bin/env python

import unittest
import os, tempfile, shutil, filecmp
import genomon_expression

class TestSimpleCount(unittest.TestCase):

    def setUp(self):
        self.parser = genomon_expression.parser.create_parser()


    def test1(self):

        cur_dir = os.path.dirname(os.path.abspath(__file__))
        tmp_dir = tempfile.mkdtemp()

        input_bam = cur_dir + "/data/bam/MCF-7_22.bam"
        output_file = tmp_dir + "/MCF-7_22.sym2fpkm.txt"
        answer_file = cur_dir + "/data/expression/MCF-7_22.sym2fpkm.txt"
        output_prefix = output_file.replace(".sym2fpkm.txt", '')

        args = self.parser.parse_args([input_bam, output_prefix, "--grc"])
        genomon_expression.run.expression_main(args)

        self.assertTrue(filecmp.cmp(output_file, answer_file, shallow=False))

        shutil.rmtree(tmp_dir)

if __name__ == "__main__":
    unittest.main()


