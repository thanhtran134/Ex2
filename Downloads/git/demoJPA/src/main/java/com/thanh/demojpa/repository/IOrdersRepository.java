package com.thanh.demojpa.repository;

import com.thanh.demojpa.entity.Orders;
import org.springframework.data.jpa.repository.JpaRepository;

public interface IOrdersRepository extends JpaRepository<Orders, Long> {
}