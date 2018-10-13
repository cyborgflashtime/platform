from syncloud_platform.config.user_config import PlatformUserConfig
from test.insider.helpers import temp_file


def test_domain():
    config = PlatformUserConfig(temp_file())
    config.init_user_config()
    
    config.update_redirect('syncloud.it', 'http://api.syncloud.it')
    assert 'syncloud.it' == config.get_redirect_domain()
    assert 'http://api.syncloud.it' == config.get_redirect_api_url()

    config.update_redirect('syncloud.info', 'http://api.syncloud.info:81')
    assert 'syncloud.info' == config.get_redirect_domain()
    assert 'http://api.syncloud.info:81' == config.get_redirect_api_url()
