TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_fault_by_id",
            "description": "故障記録IDを指定して、1件の故障情報を取得します。",
            "parameters": {
                "type": "object",
                "properties": {
                    "record_id": {
                        "type": "integer",
                        "description": "故障記録ID"
                    }
                },
                "required": ["record_id"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_faults_by_severity",
            "description": "指定された故障重大度に基づいて、該当するすべての故障情報を取得します。",
            "parameters": {
                "type": "object",
                "properties": {
                    "severity": {
                        "type": "string",
                        "description": "故障の重大度",
                        "enum": ["high", "medium", "low"]
                    }
                },
                "required": ["severity"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "count_faults_by_severity",
            "description": "指定された故障重大度に基づいて、該当する故障情報の総数を取得します。",
            "parameters": {
                "type": "object",
                "properties": {
                    "severity": {
                        "type": "string",
                        "description": "故障の重大度",
                        "enum": ["high", "medium", "low"]
                    }
                },
                "required": ["severity"]
            }
        }
    }
]