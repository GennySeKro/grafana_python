import json

import requests


class GrafanaUtils:
    def __init__(self, host, api_key):
        self.host = host
        self.api_key = api_key
        self.Headers = {'Authorization': f"Bearer {api_key}",
                        'Content-Type': 'application/json',
                        'Accept': 'application/json'}

    def Get_Folders_List(self):
        get_folders_list_url = self.host + "api/folders"
        foders_list = requests.get(get_folders_list_url, headers=self.Headers)
        return foders_list.json()
        # print(foders_list.json())

    def Create_Folder_By_UID(self, uid, title):
        create_folder_url = self.host + "api/folders"
        data = {"uid": f"{uid}",
                "title": f"{title}"}
        data = json.dumps(data)
        create_folder = requests.post(url=create_folder_url, data=data, headers=self.Headers)
        return create_folder.json()

    def Delete_Folder_By_UID(self, uid):
        delete_folder_url = self.host + 'api/folders/' + uid
        print(delete_folder_url)
        delete_folder = requests.delete(url=delete_folder_url, headers=self.Headers)
        return delete_folder

    def Create_Dashboard_by_FolderUID(self, folderuid, dashboardID='null', dashboardUID='null',
                                      overwrite=True, title='new dashboard'):
        Create_Dashboard_by_FolderUID_url = self.host + 'api/dashboards/db'
        data = json.dumps({
            "dashboard": {
                "id": dashboardID,
                "uid": dashboardUID,
                "title": f"{title}",
                "panels": [
                    {
                        "datasource": {
                            "type": "mysql",
                            "uid": "hFYb6NB4k"
                        },
                        "fieldConfig": {
                            "defaults": {
                                "color": {
                                    "mode": "palette-classic"
                                },
                                "custom": {
                                    "axisCenteredZero": False,
                                    "axisColorMode": "text",
                                    "axisLabel": "",
                                    "axisPlacement": "auto",
                                    "barAlignment": 0,
                                    "drawStyle": "line",
                                    "fillOpacity": 0,
                                    "gradientMode": "none",
                                    "hideFrom": {
                                        "legend": False,
                                        "tooltip": False,
                                        "viz": False
                                    },
                                    "lineInterpolation": "linear",
                                    "lineWidth": 1,
                                    "pointSize": 5,
                                    "scaleDistribution": {
                                        "type": "linear"
                                    },
                                    "showPoints": "auto",
                                    "spanNulls": False,
                                    "stacking": {
                                        "group": "A",
                                        "mode": "none"
                                    },
                                    "thresholdsStyle": {
                                        "mode": "off"
                                    }
                                },
                                "mappings": [],
                                "thresholds": {
                                    "mode": "absolute",
                                    "steps": [
                                        {
                                            "color": "green",
                                            "value": 'null'
                                        },
                                        {
                                            "color": "red",
                                            "value": 80
                                        }
                                    ]
                                }
                            },
                            "overrides": []
                        },
                        "gridPos": {
                            "h": 9,
                            "w": 12,
                            "x": 0,
                            "y": 0
                        },
                        "id": 2,
                        "options": {
                            "legend": {
                                "calcs": [],
                                "displayMode": "list",
                                "placement": "bottom",
                                "showLegend": True
                            },
                            "tooltip": {
                                "mode": "single",
                                "sort": "none"
                            }
                        },
                        "targets": [
                            {
                                "dataset": "flow",
                                "datasource": {
                                    "type": "mysql",
                                    "uid": "hFYb6NB4k"
                                },
                                "editorMode": "code",
                                "format": "table",
                                "rawQuery": True,
                                "rawSql": "SELECT $__time(captime), inf FROM flow.inflight ",
                                "refId": "A",
                                "sql": {
                                    "columns": [
                                        {
                                            "parameters": [
                                                {
                                                    "name": "captime",
                                                    "type": "functionParameter"
                                                }
                                            ],
                                            "type": "function"
                                        },
                                        {
                                            "parameters": [
                                                {
                                                    "name": "inf",
                                                    "type": "functionParameter"
                                                }
                                            ],
                                            "type": "function"
                                        }
                                    ],
                                    "groupBy": [
                                        {
                                            "property": {
                                                "type": "string"
                                            },
                                            "type": "groupBy"
                                        }
                                    ],
                                    "limit": 50
                                },
                                "table": "inflight"
                            }
                        ],
                        "title": "123",
                        "type": "timeseries"
                    }
                ],
                "tags": ["templated"],
                "timezone": "browser",
                "schemaVersion": 16,
                "version": 0,
                "refresh": "25s"
            },
            "folderId": 0,
            "folderUid": f"{folderuid}",
            "message": "Made changes to xyz",
            "overwrite": overwrite
        })
        print(data)
        result = requests.post(url=Create_Dashboard_by_FolderUID_url, data=data, headers=self.Headers)
        return result

