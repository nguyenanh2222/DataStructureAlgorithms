import logging
from typing import Optional, Union, Tuple

from oop.Server.Repo.user.login import login
from oop.Server.model.User.model import TemplateLogin, UserReq, AnonymusReq


class UserController:

    def login(self, template_login: TemplateLogin) -> Tuple[bool,Union[UserReq,AnonymusReq]]:
        user = login(template_login.username, template_login.password)


        print("121232")
        if user:
            user_dict = {
                'id': user.id,
                'uuid': user.uuid,
                'first_name': user.first_name,
                'middle_name': user.middle_name,
                'last_name': user.last_name,
                'username': user.username,
                'password_hash': user.password_hash,
                'password': user.password,
                'mobile': user.mobile,
                'email': user.email,
                'registered_at': user.registered_at,
                'last_login': user.last_login,
                'intro': user.intro,
                'profile': user.profile,
                'is_active': user.is_active,
                'is_reported': user.is_reported,
                'is_blocked': user.is_blocked,
            }
            return True, UserReq(
                **user_dict
            )
        else:
            return False, AnonymusReq()
