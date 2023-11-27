package dev.mikita.issueservice;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;

/**
 * The type Issue service application.
 */
@SpringBootApplication
@EnableDiscoveryClient
public class IssueServiceApplication {
	/**
	 * The entry point of application.
	 *
	 * @param args the input arguments
	 */
	public static void main(String[] args) {
		SpringApplication.run(IssueServiceApplication.class, args);
	}
}
