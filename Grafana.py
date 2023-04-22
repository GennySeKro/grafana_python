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

    def Delete_Dsahboard_By_UID(self, uid):
        delete_dashboard_url = self.host + 'api/dashboards/uid/' + uid
        delete_dashboard = requests.delete(url=delete_dashboard_url, headers=self.Headers)
        return delete_dashboard

    def Create_Dashboard_by_FolderUID(self, folderuid, dashboardID='null', dashboardUID='null',
                                      overwrite=True, title='newdashboard', database='flow',
                                      table_wapl='wapl', table_throughput='throughput', table_rtt='rtt',
                                      table_inflight='inflight'):
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
                            "h": 6,
                            "w": 10,
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
                                "rawSql": "SELECT $__time(captime), rwnd FROM " + f'{database}.' + f'{table_wapl}',
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
                                                    "name": "rwnd",
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
                                "table": "wapl"
                            }
                        ],
                        "title": "rwnd(B)",
                        "type": "timeseries"
                    },
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
                            "overrides": [
                                {
                                    "matcher": {
                                        "id": "byName",
                                        "options": "throughput"
                                    },
                                    "properties": [
                                        {
                                            "id": "color",
                                            "value": {
                                                "fixedColor": "#3917d8",
                                                "mode": "fixed"
                                            }
                                        }
                                    ]
                                }
                            ]
                        },
                        "gridPos": {
                            "h": 12,
                            "w": 11,
                            "x": 10,
                            "y": 0
                        },
                        "id": 8,
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
                                "rawSql": "SELECT $__time(captime), throughput FROM " + f'{database}.' + f'{table_throughput}',
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
                                                    "name": "throughput",
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
                                "table": "throughput"
                            }
                        ],
                        "title": "throughput(B/0.1s)",
                        "type": "timeseries"
                    },
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
                            "overrides": [
                                {
                                    "matcher": {
                                        "id": "byName",
                                        "options": "pktlen"
                                    },
                                    "properties": [
                                        {
                                            "id": "color",
                                            "value": {
                                                "mode": "continuous-GrYlRd"
                                            }
                                        }
                                    ]
                                }
                            ]
                        },
                        "gridPos": {
                            "h": 6,
                            "w": 10,
                            "x": 0,
                            "y": 6
                        },
                        "id": 4,
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
                                "rawSql": "SELECT $__time(captime), pktlen FROM " + f'{database}.' + f'{table_wapl}',
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
                                                    "name": "pktlen",
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
                                "table": "wapl"
                            }
                        ],
                        "title": "pktlen(B)",
                        "type": "timeseries"
                    },
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
                            "overrides": [
                                {
                                    "matcher": {
                                        "id": "byName",
                                        "options": "rtt"
                                    },
                                    "properties": [
                                        {
                                            "id": "color",
                                            "value": {
                                                "mode": "fixed",
                                                "seriesBy": "last"
                                            }
                                        }
                                    ]
                                }
                            ]
                        },
                        "gridPos": {
                            "h": 8,
                            "w": 10,
                            "x": 0,
                            "y": 12
                        },
                        "id": 6,
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
                                "rawSql": "SELECT $__time(captime), rtt FROM " + f'{database}.' + f'{table_rtt}',
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
                                                    "name": "rtt",
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
                                "table": "rtt"
                            }
                        ],
                        "title": "rtt(ms)",
                        "type": "timeseries"
                    },
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
                            "overrides": [
                                {
                                    "matcher": {
                                        "id": "byName",
                                        "options": "inf"
                                    },
                                    "properties": [
                                        {
                                            "id": "color",
                                            "value": {
                                                "fixedColor": "#e8d617",
                                                "mode": "fixed"
                                            }
                                        }
                                    ]
                                }
                            ]
                        },
                        "gridPos": {
                            "h": 8,
                            "w": 11,
                            "x": 10,
                            "y": 12
                        },
                        "id": 10,
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
                                "rawSql": "SELECT $__time(captime), inf FROM " + f'{database}.' + f'{table_inflight}',
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
                        "title": "inflight(B)",
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
