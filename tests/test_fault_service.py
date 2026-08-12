from app.services import fault_service


# 中文：测试根据ID查询故障
def test_get_fault_by_id_success():
    result = fault_service.get_fault_by_id(1)

    assert result["success"] is True
    assert result["fault"]["id"] == 1


# 中文：测试非法ID
def test_get_fault_by_id_invalid():
    result = fault_service.get_fault_by_id(-1)

    assert result["success"] is False


# 中文：测试severity统计
def test_count_faults_by_severity():
    result = fault_service.count_faults_by_severity("high")

    assert result["success"] is True
    assert result["count"] >= 0