from system.file import File
import json


class Json(File):
    def __init__(self, name):
        File.__init__(self, name)

    def f_read(self):
        return json.loads(super().f_read())

    def f_write(self, data):
        d = json.dumps(data)
        super().f_write(d)





if __name__ == "__main__":
    j = Json("captor.json")
    j.f_write({'Alice': 89, 'Bob': 72, 'Charles': 87})
    print(j.f_read())
