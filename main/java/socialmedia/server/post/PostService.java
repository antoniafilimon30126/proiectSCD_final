package socialmedia.server.post;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.Optional;

@Service
public class PostService {

    @Autowired
    private PostRepository postRepository;

    @Transactional
    public Post create(Post myPost) {
        return postRepository.save(myPost);
    }

    public List<Post> findAllPosts(){
        return postRepository.findAll();
    }


    @Transactional
    public Post update(Integer id, Post post) {
        Optional<Post> existingPost = postRepository.findById(id);
        if (existingPost.isPresent()) {
            Post p = existingPost.get();
            p.setTitle(post.getTitle());
            p.setContent(post.getContent());
            p.setStatus(post.getStatus());
            p.setUser(post.getUser());
            return postRepository.save(p);
        }
        return null;
    }

    @Transactional
    public void delete(Integer id) {
        postRepository.deleteById(id);
    }
}
