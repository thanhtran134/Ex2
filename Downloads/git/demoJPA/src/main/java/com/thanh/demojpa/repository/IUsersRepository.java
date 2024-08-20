package com.thanh.demojpa.repository;

import com.thanh.demojpa.entity.Users;
import org.springframework.data.jpa.repository.JpaRepository;

public interface IUsersRepository extends JpaRepository<Users, Long> {
    public Users findByUsername(String username);
}
