import unittest
import json
from Courses import Course, Course_Progress,app,db

#################################Done by Sun Yuyang#######################
class TestCourse(unittest.TestCase):
    test4 = Course_Progress(progress_id='1 C101-C1', engineer_id='1', course_id='C101', lesson= 'C101-L1', pdf_material='pdf1.pdf', ppt_material='ppt1.pptx',video_material="vid1.mp4",doc_material="doc1.docx",quiz_id="quiz_1")
    def test_data(self):
        self.assertEqual(self.test4.to_dict(), {
            'progress_id': '1 C101-C1',
            'engineer_id': '1',
            'course_id': 'C101',
            'lesson': 'C101-L1',
            'pdf_material': 'pdf1.pdf',
            'ppt_material': 'ppt1.pptx',
            'video_material': 'vid1.mp4',
            'doc_material': 'doc1.docx',
            'quiz_id': 'quiz_1'
        }
        )


          ###check if the course id engineer_id in progress_class_id and the progress_idd match#####
    def test_progress_id(self):
        course_id = self.test4.to_dict()['course_id']
        engineer_id = self.test4.to_dict()['engineer_id']
        progress_id_inserted=engineer_id+' '+course_id+'-'+'C1'
        progress_id=self.test4.to_dict()['progress_id']
        self.assertEqual(progress_id, progress_id_inserted)



if __name__ == '__main__':
    unittest.main()
