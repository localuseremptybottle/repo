class LocatorsMyAccount:
    #MyAccount
    MyAccountButton = '//*[@id="page"]/header[1]/div/div/div/ul/li[3]/a'
    MyAccountLoginInput = '//*[@id="username"]'
    MyAccountLoginPasswordInput = '//*[@id="password"]'
    MyAccountLoginButton = '//*[@id="customer_login"]/div[1]/form/p[3]/input[3]'

    MyAccountRemembermecheckbox ='//*[@id="rememberme"]'
    MyAccountLostyourPasswordButton = '//*[@id="customer_login"]/div[1]/form/p[4]/a'
    MyAccountErrorIncorectPasswordtext ="//li[contains(., 'The password you entered for the username slonagrafika@gmail.com is incorrect.')]"
    MyAccountErrorIncorectEmailtext ="//li[contains(., 'A user could not be found with this email address.')]"


    #LostPassword
    MyAccountRecorveryUsernameInput = '//input[@id="user_login"]'
    MyAccountRecorveryResetPasswordButton = '//*[@id="post-8"]/div[2]/form/p[3]/input[2]'
    MyAccountRecorveryErrorTextEnterUsername= "//li[contains(., 'Enter a username or email address.')]"
    MyAccountRecorveryErrorTextInvalidUsername= "//li[contains(., 'Invalid username or email')]"
    MyAccountRecorveryPositiveTextEmailResetText = "//div[contains(., 'Password reset email has been sent.')]"

    #DashboardTab
    MyAccountDashboardTab = '//a[@href="https://skleptest.pl/my-account/" and text()="Dashboard"]'
    MyAccountOrdersTab =    '//a[@href="https://skleptest.pl/my-account/" and text()="Orders"]'
    MyAccountDownloadsTab = '//*[@id="post-8"]/div[2]/nav/ul/li[3]/a'
    MyAccountAddressesTab = '//*[@id="post-8"]/div[2]/nav/ul/li[4]/a'
    MyAccountAccountDetailsTab = '//*[@id="post-8"]/div[2]/nav/ul/li[5]/a'
    MyAccountAccountLogoutTab = '//*[@id="post-8"]/div[2]/nav/ul/li[6]/a'
    MyAccountDashboardTabRecentOrderdslinktext = 'recent orders'
    MyAccountDashboardTabShippingadresslinktext = 'shipping and billing addresses'
    MyAccountDashboardTabEditPasswordlinktext = 'edit your password and account details'
    MyAccountLogoutTabConfirmandLogoutlinktext ='//*[@id="post-8"]/div[2]/div[1]/a'
    #OrdersTab
    MyAccountOrdersTab1Productviewbutton = '//*[@id="post-8"]/div[2]/div/table/tbody/tr[1]/td[5]/a'
    MyAccountOrdersTab2Productviewbutton = '//*[@id="post-8"]/div[2]/div/table/tbody/tr[2]/td[5]/a'
    MyAccountOrdersTabOrderDetailstext= 'Order details'
    MyAccountOrdersTabOrderDetailsPrint = '//*[@id="post-8"]/div[2]/div/section[2]/h3/a'