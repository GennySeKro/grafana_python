import Grafana

Host = "http://101.43.161.79:3000/"
api_key = "eyJrIjoibk4zcm5HTWI2aGlqbkN2R1lHNlhETlFEWnZVRlFLcHciLCJuIjoidGVzdCIsImlkIjoxfQ=="

# result = Grafana.GrafanaUtils(Host, api_key)
# print(result.Get_Folders_List())
result = Grafana.GrafanaUtils(host=Host, api_key=api_key)
# result.Create_Folder_By_UID(uid="123", title="测试")
# result.Delete_Folder_By_UID('123')

print(result.Create_Dashboard_by_FolderUID(folderuid='123', dashboardID='test_dashboard',
                                           dashboardUID='123456'))
