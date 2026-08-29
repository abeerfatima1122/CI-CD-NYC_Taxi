def test_payment_type_has_valid_values():
    chunk = pd.DataFrame({
        'payment_type': [1, 2, 3, 4, 5, 6]
    })

    assert chunk['payment_type'].isin([1, 2, 3, 4, 5, 6]).all()


def test_ratecode_id_has_valid_values():
    chunk = pd.DataFrame({
        'RatecodeID': [1, 2, 3, 4, 5, 6]
    })

    assert chunk['RatecodeID'].isin([1, 2, 3, 4, 5, 6]).all()


def test_store_and_forward_flag():
    chunk = pd.DataFrame({
        'store_and_fwd_flag': ['Y', 'N']
    })

    assert chunk['store_and_fwd_flag'].isin(['Y', 'N']).all()


def test_dropoff_time_after_pickup_time():
    chunk = pd.DataFrame({
        'tpep_pickup_datetime': pd.to_datetime([
            '2026-01-01 10:00:00',
            '2026-01-01 12:00:00'
        ]),
        'tpep_dropoff_datetime': pd.to_datetime([
            '2026-01-01 10:30:00',
            '2026-01-01 12:20:00'
        ])
    })

    assert (
        chunk['tpep_dropoff_datetime'] >
        chunk['tpep_pickup_datetime']
    ).all()