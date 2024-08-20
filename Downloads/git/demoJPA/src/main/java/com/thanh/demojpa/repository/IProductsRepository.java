package com.thanh.demojpa.repository;

import com.thanh.demojpa.entity.Products;
import org.springframework.data.jpa.repository.JpaRepository;

public interface IProductsRepository extends JpaRepository<Products, Long> {
}
