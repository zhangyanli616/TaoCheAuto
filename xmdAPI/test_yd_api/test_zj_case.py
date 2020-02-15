#自建工单case


from xmdAPI.base import Base
from xmdAPI.test_yd_api.common_fuc import helpZj
from xmdAPI.test_yd_api.common_fuc import setPhoneNumber



class TestZJCase(Base):

    '''
            {"clueChannelName":"分销",（渠道来源Name 必填）
            "clueChannelId":"1170",（渠道来源ID 必填）
            "customerName":"${phoneNum}",（客户姓名 必填）
            "customerPhone":"${phoneNum}",（客户手机号 必填）
            "purchaseMode":"1",(1分期，0全款 必填)
            "customerType":"1",（1个人，2公司 必填）
            "carCode":"${newCarCode}",（车源编号 必填）
            "gender": "0",（1:男 0:女 非必填）
            "sparePhone":"199283993",(备用手机 非必填)
            "remark":"1111" (备注 非必填)}
            '''


    #自建工单失败，clueChannelId参数为空
    def test_zj_clueIdEmpty(self):
        print(setPhoneNumber())
        result = helpZj("分销","","张三",setPhoneNumber(),"1","1","000552648","0","18829300332","备注")
        self.assertEqual(result['message'],"渠道不能为空")

    #自建工单失败，customerName名字长度大于200字符
    def test_zj_customerNameLong(self):
        print(setPhoneNumber())
        result = helpZj("分销","1170",
                        "张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三张三",
                        setPhoneNumber(),"1","1","000552648","0","18829300332","备注")
        self.assertEqual(result['message'],"保存客户信息异常，请稍后重试!")

    #自建工单失败，customerPhone参数为空
    def test_zj_customerPhoneEmpty(self):
        result = helpZj("分销","1170","张三","","1","1","000552648","0","18829300332","备注")
        self.assertEqual(result['message'],"客户手机号不能为空")

    #自建工单失败，purchaseMode参数为空
    def test_zj_purchaseModeEmpty(self):
        result = helpZj("分销","1170","张三",setPhoneNumber(),"","1","000552648","0","18829300332","备注")
        self.assertEqual(result['message'],"购车方式不能为空")

    #自建工单失败，customerType参数为空
    def test_zj_customerTypeEmpty(self):
        result = helpZj("分销","1170","张三",setPhoneNumber(),"1","","000552648","0","18829300332","备注")
        self.assertEqual(result['message'],"客户类型不能为空")

    #自建工单失败，carCode参数为空
    def test_zj_carCodeEmpty(self):
        result = helpZj("分销","1170","张三",setPhoneNumber(),"1","1","","0","18829300332","备注")
        self.assertEqual(result['message'],"意向车型不能为空")

    #自建工单成功，clueChannelName不校验
    def test_zj_clueNameEmpty(self):
        result = helpZj("","1170","张三",setPhoneNumber(),"1","1","000552648","0","18829300332","备注")
        self.assertTrue(result['success'], True)

    #自建工单成功，clueChannelId只校验非空
    def test_zj_clueIdUnusual(self):
        result = helpZj("分销","11889","张三",setPhoneNumber(),"1","1","000552648","0","18829300332","备注")
        self.assertTrue(result['success'], True)

    #自建工单成功，customerName只校验长度不能大于200
    def test_zj_customerNameEmpty(self):
        result = helpZj("分销","1170","",setPhoneNumber(),"1","1","000552648","0","18829300332","备注")
        self.assertTrue(result['success'], True)

    #自建工单成功，customerPhone只校验非空
    def test_zj_customerPhoneUnusual(self):
        result = helpZj("分销","1170","张三",setPhoneNumber(),"1","1","000552648","0","18829300332","备注")
        print(result)
        self.assertTrue(result['success'], True)

    #自建工单成功，purchaseMode只校验非空
    def test_zj_purchaseModeUnusual(self):
        result = helpZj("分销","1170","张三",setPhoneNumber(),"2","1","000552648","0","18829300332","备注")
        self.assertTrue(result['success'], True)

    # 自建工单成功，carCode只校验非空
    def test_zj_carCodeUnusual(self):
        result = helpZj("分销", "1170", "张三", setPhoneNumber(), "1", "1", "111", "0", "18829300332", "备注")
        self.assertTrue(result['success'], True)

    #自建工单成功，gender字段不校验
    def test_zj_genderEmpty(self):

        result = helpZj("分销","1170","张三",setPhoneNumber(),"1","1","12323","","18829300332","备注")
        self.assertTrue(result['success'], True)

    #自建工单成功，sparePhone字段不校验
    def test_zj_sparePhoneEmpty(self):
        result = helpZj("分销","1170","张三",setPhoneNumber(),"1","1","12323","1","","备注")
        self.assertTrue(result['success'], True)

    #自建工单成功，remark字段不校验
    def test_zj_remarkEmpty(self):
        result = helpZj("分销","1170","张三",setPhoneNumber(),"1","1","12323","1","123213","")
        self.assertTrue(result['success'], True)

    #自建工单成功
    def test_zj_success(self):
        result = helpZj("分销","1170","张三",setPhoneNumber(),"1","1","000552648","0","18829300332","备注")
        self.assertTrue(result['success'],True)

    #自建工单成功后，返回手机号
    def get_zj_phone(self):
        myPhone = setPhoneNumber()
        result = helpZj("分销","1170","张三",myPhone,"1","1","000552648","0","18829300332","备注")
        return myPhone