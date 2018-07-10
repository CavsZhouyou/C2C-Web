from app import app 
import unittest 

#用户相关的测试
class UserTestCase(unittest.TestCase):
    
    def setUp(self):
        app.config['TESTING'] = True 
        self.app = app.test_client()
        
    def tearDown(self):
        pass

    def test_a_index(self):
        rv = self.app.get('/') 
        data = rv.get_json()
        print("get index return",data,"\n")
        assert 'success' in data 
    
    #def test_registe(self):
    #    rv = self.app.post('/c2c/regist',json={
    #        'nickname':"unittest",
    #        'password':"password",
    #        'email':"333@qq.com",
    #        'phone':"17863110520",
    #        'role_id':"4",
    #        'name':"blame",
    #        'id_card':"3242747278637673617"
    #        })
    #    data = rv.get_json()
    #    print("regist return ",data,"\n")
    #    assert data['success']
    
    def test_b_login(self):
        rv = self.app.post('/c2c/login',json={
            'email':"333@qq.com",
            'password':'password'})
        data = rv.get_json()
        print("login return ",data,"\n")
        assert "user_id" in data 

    def test_c_userinfo(self):
        with app.test_request_context("/c2c/userinfo"):
            self.app.post('/c2c/login',json={
            'email':"333@qq.com",
            'password':'password'})

            app.preprocess_request()
            rv = self.app.get('/c2c/userinfo')
            data = rv.get_json()
            print("userinfo return ",data,"\n")
            assert "success" not in data
    
    def test_d_userupdate(self):
        with app.test_request_context("/c2c/userinfo"):
            self.app.post('/c2c/login',json={
            'email':"333@qq.com",
            'password':'password'})

            app.preprocess_request()
            rv = self.app.post('/c2c/userupdate',json={
                                'nickname':'testuser',
                                'phone':"111111",
                                "name":"bbbn",
                                "id_card":"3422712732376"})
            data = rv.get_json()
            print("userupdate return ",data,"\n")
            assert data['success']

    def test_e_passwordchange(self):
        with app.test_request_context("/c2c/userinfo"):
            self.app.post('/c2c/login',json={
            'email':"333@qq.com",
            'password':'password'})

            app.preprocess_request()
            rv = self.app.post('/c2c/changepassword',json={
                                'password':"password"})
            data = rv.get_json()
            print("password change return ",data,"\n")
            assert data['success']
         

    def test_z_logout(self):
        rv = self.app.get('/c2c/logout')
        data = rv.get_json()
        print("logout return ",data,"\n")
        assert data['success']


#房源信息相关的测试
class PublishAccommodation(unittest.TestCase):
    
    def setUp(self):
        app.config['TESTING'] = True 
        self.app = app.test_client()
        
    def tearDown(self):
        pass

    def login(self):
        rv = self.app.post('/c2c/login',json={
            'email':"333@qq.com",
            'password':'password'})
        data = rv.get_json()
        if(data['success']):
            return data['user_id']
        else:
            return False 

    def test_a_publish(self):
        with app.test_request_context("/c2c/userinfo"):
            user_id = self.login()
            app.preprocess_request()
            if(user_id):
                rv = self.app.post('/c2c/accommodation/add',json={
                    'acc_address':'weihai',
                    'acc_capacity':300,
                    'acc_price':"6000",
                    'acc_city':1,
                    'acc_description':"nothing",
                    'acc_user_id':3,
                    'acc_type_id':1
                    })
                data = rv.get_json()
                print("accommodation return ",data,"\n")
                assert data['success']
            else:
                return False 

    def test_b_list(self):
        rv = self.app.post('/c2c/accommodation/list',json={
            'index':1})
        data = rv.get_json()
        print("Accommodation list return ",data,'\n')
        assert 'success' not in data 

    def test_c_show(self):
        rv = self.app.get('/c2c/accommodation/show/1')
        data = rv.get_json()
        print("Accommodation show ",data,"\n")
        assert 'success' not in data 

    def test_d_del(self):
        with app.test_request_context("/c2c/del_one_accommodation/1"):
            user_id = self.login()
            app.preprocess_request()
            if(user_id):
                rv = self.app.post('/c2c/del_one_accommodation/1')
                data = rv.get_json()
                print("accommodation return ",data,"\n")
                assert data['success']
            else:
                return False 



if __name__=='__main__':
    unittest.main()
