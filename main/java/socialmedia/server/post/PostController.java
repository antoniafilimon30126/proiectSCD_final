package socialmedia.server.post;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/post")
@CrossOrigin
public class PostController {

    @Autowired
    private PostService postService;

    @PostMapping
    public Post create(@RequestBody Post myPost)
    {
        return postService.create(myPost);
    }

    @GetMapping
    public List<Post> getAllPosts(){
        return postService.findAllPosts();
    }

    @PutMapping("/{id}")
    public Post updatePost(@PathVariable Integer id, @RequestBody Post post) {
        return postService.update(id, post);
    }

    @DeleteMapping("/{id}")
    public void deletePost(@PathVariable Integer id) {
        postService.delete(id);
    }
}
