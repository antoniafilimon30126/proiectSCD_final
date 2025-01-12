package socialmedia.server.comment;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.hibernate.annotations.CreationTimestamp;
import socialmedia.server.user.User;
import socialmedia.server.post.Post;  // Corect importul pentru Post

import java.util.Date;

@Entity
@AllArgsConstructor
@NoArgsConstructor
@Data
public class Comment {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @ManyToOne
    @JoinColumn(name = "post_id", nullable = false)
    private Post post;


    @ManyToOne
    @JoinColumn(name="user_id", nullable = false)  // Corect legătura cu User
    private User user;

    @CreationTimestamp
    @Column(updatable = false, nullable = false)
    private Date createdOn;

    private String content;
}
