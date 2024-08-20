package com.thanh.demojpa.repository;

import com.thanh.demojpa.entity.OrderDetails;
import org.springframework.data.jpa.repository.JpaRepository;

public interface IOrderDetailsRepository extends JpaRepository<OrderDetails, Long> {
}