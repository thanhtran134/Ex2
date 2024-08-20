package com.thanh.demojpa.controller;

import com.thanh.demojpa.entity.Products;
import com.thanh.demojpa.repository.IProductsRepository;
import com.thanh.demojpa.service.UsersService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import java.util.List;

@Controller
public class HomeController {
    @Autowired
    PasswordEncoder passwordEncoder;
    @Autowired
    UsersService userService;

    //Demo nen dung truc tiep product repository
    @Autowired
    IProductsRepository productRepository;

    @GetMapping("/")
    public String welcome(final Model model)
    {
        List<Products> lstProducts = productRepository.findAll();
        model.addAttribute("products", lstProducts);

        return "welcome";
    }

    @GetMapping("/home")
    public String Home()
    {
        return "welcome";
    }
}
