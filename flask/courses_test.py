import unittest

from Courses import Course, Course_Class, Course_Lesson


# Done by Mayuri Milind Salunke
class TestCourse(unittest.TestCase):
    c1 = Course(course_id='C101', course_name='Basic Mathematics', course_type='Assigned', course_prerequisite= None, course_brief='This is a Year1 course which would be required to be completed prior to C201 Intermediate Mathematics', course_class='C101-C1, C101-C2, C101-C3', lessons='C101-L1, C101-L2, C101-L3, C101-L4', start_date='2021-10-25 09:00:00', end_date='2022-02-25 09:00:00')
    def test_to_dict(self):
        self.assertEqual(self.c1.to_dict(), {
            'course_id': 'C101',
            'course_name': 'Basic Mathematics',
            'course_type': 'Assigned',
            'course_prerequisite': None,
            'course_brief': 'This is a Year1 course which would be required to be completed prior to C201 Intermediate Mathematics',
            'course_class': 'C101-C1, C101-C2, C101-C3',
            'lessons': 'C101-L1, C101-L2, C101-L3, C101-L4',
            'start_date': '2021-10-25 09:00:00',
            'end_date': '2022-02-25 09:00:00'
        }
        )




# Done by Mayuri Milind Salunke
class TestCourse_Class(unittest.TestCase):
    cc1 = Course_Class(course_class_id='C101-C1', course_id='C101', seats_available=20)
    def test_to_dict(self):
        self.assertEqual(self.cc1.to_dict(), {
            'course_class_id': 'C101-C1',
            'course_id': 'C101',
            'seats_available': 20
        }
        )
    # Test Seats available are greater or equal to 0
    def test_seats_available(self):
        self.assertGreater(self.cc1.to_dict()['seats_available'], -1)

    # Test Course Class ID is in the correct format 
    def test_course_class_id(self):
        self.assertIn(self.cc1.to_dict()['course_class_id'].split('-')[1][0], 'C')

    # Test Course in Course Class ID is correct 
    def test_course_id(self):
        course_id = self.cc1.to_dict()['course_class_id'].split('-')[0]
        original_course_id = self.cc1.to_dict()['course_id']
        self.assertEqual(course_id, original_course_id)





# Done by Mayuri Milind Salunke
class TestCourse_Lesson(unittest.TestCase):
    cl1 = Course_Lesson(course_lesson_id='C101-L1', course_id='C101', pdf_material='pdf1.pdf, pdf2.pdf', ppt_material='ppt1.pptx, ppt2.pptx', video_material='vid1.mp4, vid2.mp4, vid3.mp4', doc_material='doc1.docx, doc2.docx, doc3.docx', quiz_id=None,)
    def test_to_dict(self):
        self.assertEqual(self.cl1.to_dict(), {
            'course_lesson_id': 'C101-L1',
            'course_id': 'C101',
            'pdf_material': 'pdf1.pdf, pdf2.pdf',
            'ppt_material': 'ppt1.pptx, ppt2.pptx',
            'video_material': 'vid1.mp4, vid2.mp4, vid3.mp4',
            'doc_material': 'doc1.docx, doc2.docx, doc3.docx',
            'quiz_id': None,
        }
        )

    # Test Course Lesson ID is in the correct format 
    def test_course_class_id(self):
        self.assertIn(self.cl1.to_dict()['course_lesson_id'].split('-')[1][0], 'L')

    # Test Course in Course Class ID is correct 
    def test_course_id(self):
        course_id = self.cl1.to_dict()['course_lesson_id'].split('-')[0]
        original_course_id = self.cl1.to_dict()['course_id']
        self.assertEqual(course_id, original_course_id)

    # Check if materials are in the right format
    def test_course_material(self):
        pdf_material = 'pdf'
        ppt_material = ['pptx', 'ppt']
        doc_material = ['doc', 'docx']
        video_material = ['mp4', 'avi', 'mpeg']

        pdf_materials = self.cl1.to_dict()['pdf_material']
        for pdf in pdf_materials.split(','):
            self.assertIn(pdf.split('.')[1],pdf_material)
        
        ppt_materials = self.cl1.to_dict()['ppt_material']
        for ppt in ppt_materials.split(','):
            self.assertIn(ppt.split('.')[1],ppt_material)
        
        doc_materials = self.cl1.to_dict()['doc_material']
        for doc in doc_materials.split(','):
            self.assertIn(doc.split('.')[1],doc_material)

        video_materials = self.cl1.to_dict()['video_material']
        for video in video_materials.split(','):
            self.assertIn(video.split('.')[1],video_material)
    



if __name__ == '__main__':
    unittest.main()