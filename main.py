import Grafana

# Host = "服务器地址"
# api_key = "鉴权令牌"

# result = Grafana.GrafanaUtils(Host, api_key)
# print(result.Get_Folders_List())
result = Grafana.GrafanaUtils(host=Host, api_key=api_key)
# result.Create_Folder_By_UID(uid="123", title="测试")
# result.Delete_Folder_By_UID('123')

result.Delete_Dsahboard_By_UID('123456')
# result.Create_Dashboard_by_FolderUID(folderuid='123', dashboardID='test_dashboard123',
#                                      dashboardUID='1234567')
# result.Create_Dashboard_by_FolderUID(folderuid='123', dashboardID='test_dashboard',
#                                      dashboardUID='123456789', title='test')
