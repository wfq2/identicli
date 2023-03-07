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

    def test_adding_user_identicon(self):
        service = IdenticonService()
        service.create_user_identicon("wyatt")
        assert service._count == 1
        assert service._db['wyatt']

    def test_adding_many_user_identicons(self):
        service = IdenticonService()
        for i in range(20):
            service.create_user_identicon(str(i))
        assert service._count == 20
        for i in range(20):
            if str(i) not in service._db:
                raise Exception(f"{i} not in test database")
