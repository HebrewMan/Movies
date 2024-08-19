# from djoser import error_messages as default_error_messages

def response_data(status_code=0, message=None, data={}, **kwargs):
    return dict({
        'status_code': status_code,
        'message': message,
        'data': data
    }, **kwargs)

class VerificationCodeError(object):
    VerificationNotMatch = (100001, '验证码错误')

class ProfileError(object):
    ProfileNotFound = (200001, '用户信息不存在')
    MemberNotExists = (200002, '非会员用户无法查看')
    MemberHasExpired = (200003, '会员已过期')

class UserError(object):
    UserNotFound = (300001, '用户名不存在')
    PasswordError = (300002, '密码错误')
    UserHasExists = (300003, '该用户名已经存在')
    UserHasSentEmail = (300004, '已经发送邮箱')
    UserSendEmailFailed = (300005, '邮箱发送失败')
    PhoneHasExists = (300006, '手机号已经存在')
    UserNotLogin = (300007, '请先登录')
    PasswordInconsistent = (300008, '2次密码不一致')

class MovieError(object):
    MovieParamError = (500001, '电影参数错误')
    MovieCollectError = (500002, '电影收藏异常')
    MovieNotFound = (50003, '电影信息不存在')


    