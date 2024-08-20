package com.thanh.demojpa.entity;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.List;

@Entity
@Table(name = "Catalogs")
@Data
@NoArgsConstructor
@AllArgsConstructor
public class Catalogs {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long Id;

    @Column(name = "name", length = 150, nullable = false)
    private String name;

    @Column(name = "status", nullable = false)
    private boolean status;

    @OneToMany(mappedBy = "catalog", cascade = CascadeType.ALL, fetch = FetchType.LAZY)
    private List<Products> products;

    // Getters and Setters
}