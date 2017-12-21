from wand.image import Image
from settings import settings
from models.file import File
from models.user import User
import time
import os


class FileUploader:
    @staticmethod
    def pdf_to_images(filename, file_id):
        """Split PDF into PNGs
        PNGs are being uploaded to a folder with the same name as PDF file has
        """
        all_pages = Image(filename='{}/{}'.format(settings['static_path'], filename))
        file_id_dir = '{}/{}'.format(settings['static_path'], file_id)
        if not os.path.exists(file_id_dir):
            os.makedirs(file_id_dir)

        for i, page in enumerate(all_pages.sequence):
            with Image(page) as img:
                img.save(filename='{}/{}.png'.format(file_id_dir, i))

        return len(all_pages.sequence)

    def save_pdf(self, file, username):
        """Saving the uploaded file if is PDF
        """
        content_type = file['content_type']
        if self.is_pdf(content_type):
            index = file['filename'].rfind(".")
            file_id = self.generate_filename()
            filename = file_id + file['filename'][index:]
            with open('{}/{}'.format(settings['static_path'], filename), "wb") as out:
                out.write(file['body'])
                length = self.pdf_to_images(filename, file_id)
                self.save_fileinfo_to_db(username, file_id, content_type, length)

    @staticmethod
    def is_pdf(content_type):
        """Does this content_type corresponds to PDF
        """
        return content_type == 'application/pdf'

    @staticmethod
    def save_fileinfo_to_db(username, file_id, content_type, file_length):
        """Save info about file into DB
        """
        user = User.get(User.username == username)
        File.create(filename=file_id, type=content_type, user=user, length=file_length)

    @staticmethod
    def generate_filename():
        """Filename generation based on current timestamp
        """
        return str(time.time()).replace(".", "")
