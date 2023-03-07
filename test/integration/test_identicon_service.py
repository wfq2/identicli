from identicon_service import IdenticonService


class TestIdenticonService:

    def test_saving_loading(self):
        service = IdenticonService.load()
        service.create_user_identicon('test_user')
        assert service._count == 1
        service.save()
        new_service = IdenticonService.load()
        assert new_service._count == 1
        assert new_service._db['test_user']